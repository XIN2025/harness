from __future__ import annotations

import json
from pathlib import Path

from oracle_eval.oracle.projection import ScopeKind, project_index
from oracle_eval.paths import is_test_file
from oracle_eval.scip.load import load_index
from oracle_eval.scip.symbols import short_name

DATA = Path(__file__).parent.parent / "data" / "oracle" / "remeda"

KNOWN_SCIP_FALSE_POSITIVES = {"call", "cancel", "flush"}

Edge = tuple[str, str, str]


def scip_edges() -> set[Edge]:
    edges = project_index(load_index(DATA / "index.jsonl"), "remeda")
    return {
        (e.file.replace("\\", "/"), short_name(e.caller), short_name(e.callee))
        for e in edges
        if e.in_repo and not e.is_test_file and e.caller_kind is ScopeKind.FUNCTION
    }


def tsmorph_edges() -> tuple[set[Edge], set[Edge]]:
    calls: set[Edge] = set()
    refs: set[Edge] = set()
    with (DATA / "tsmorph2.jsonl").open(encoding="utf8") as fh:
        for line in fh:
            record = json.loads(line)
            if "error" in record:
                continue
            path = record["relative_path"].replace("\\", "/")
            if is_test_file(path):
                continue
            for c in record.get("calls", []):
                calls.add((path, c["caller"], c["callee_text"]))
            for c in record.get("callable_refs", []):
                refs.add((path, c["caller"], c["callee_text"]))
    return calls, refs


def main() -> None:
    scip = scip_edges()
    calls, refs = tsmorph_edges()
    oracle = calls | refs

    gap = scip - calls
    covered = gap & refs
    residual = gap - refs
    false_positives = {e for e in residual if e[2] in KNOWN_SCIP_FALSE_POSITIVES}
    unexplained = residual - false_positives

    print(f"SCIP edges (in-repo, non-test, function caller) : {len(scip):>5}")
    print(f"ts-morph call expressions                       : {len(calls):>5}")
    print(f"ts-morph callable references                    : {len(refs):>5}")
    print(f"ORACLE = calls + callable refs                  : {len(oracle):>5}")
    print()
    print(f"the gap SCIP used to fill                       : {len(gap):>5}")
    print(
        f"  now covered by callable refs                  : {len(covered):>5}"
        f"  ({len(covered) / len(gap):.1%})"
    )
    print(f"  known SCIP false positives (correctly absent) : {len(false_positives):>5}")
    print(f"  UNEXPLAINED -- real misses                    : {len(unexplained):>5}")
    for edge in sorted(unexplained):
        print(f"      {edge}")
    print()
    adjusted = len(covered) / (len(gap) - len(false_positives)) if gap else 0.0
    print(f"coverage of SCIP's *valid* contribution         : {adjusted:.1%}")
    print()
    print(f"oracle edges SCIP could never see               : {len(oracle - scip):>5}")
    print("  (locals, parameters, node_modules -- SCIP has no name for these)")


if __name__ == "__main__":
    main()
