import type { Interval } from "./types";

export function pct(value: number, digits = 1): string {
  return `${(value * 100).toFixed(digits)}%`;
}

export function pctValue(value: number, digits = 1): string {
  return (value * 100).toFixed(digits);
}

export function withInterval(interval: Interval): string {
  return `${pct(interval.point)} [${intervalRange(interval)}]`;
}

export function intervalRange(interval: Interval): string {
  return `${pctValue(interval.low)}-${pctValue(interval.high)}`;
}
