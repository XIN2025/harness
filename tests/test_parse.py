from oracle_eval.predict.parse import ParseResult, ValidityReport, parse_response

GOOD = '{"calls": [{"caller": "add", "callee_text": "purry", "kind": "free", "line": 36}]}'


def test_fenced_json_is_parseable_but_not_raw_valid() -> None:
    result = parse_response(f"```json\n{GOOD}\n```")
    assert (result.raw_valid, result.parseable, result.schema_valid) == (False, True, True)


def test_prose_around_unfenced_json_is_unparseable_on_purpose() -> None:
    result = parse_response(f"Here are the calls I found:\n{GOOD}")
    assert not result.parseable
    assert result.error is not None


def test_valid_json_that_misses_a_required_field_is_schema_invalid_not_unparseable() -> None:
    result = parse_response('{"calls": [{"caller": "add"}]}')
    assert (result.raw_valid, result.parseable, result.schema_valid) == (True, True, False)
    assert "callee_text" in (result.error or "")


def test_missing_calls_key_is_not_the_same_as_an_empty_answer() -> None:
    assert not parse_response("{}").schema_valid
    empty = parse_response('{"calls": []}')
    assert empty.schema_valid
    assert empty.prediction is not None and empty.prediction.calls == []


def test_the_report_keeps_the_denominator_attached() -> None:
    report = ValidityReport()
    report.add(ParseResult(True, True, True))
    report.add(ParseResult(False, True, False, error="boom"))
    report.add(ParseResult(False, False, False, error="not JSON"))

    assert (report.raw_valid, report.parseable, report.schema_valid) == (1, 2, 1)
    assert report.schema_valid_rate == 1 / 3
    assert "1/3" in report.render()
    assert len(report.errors) == 2
