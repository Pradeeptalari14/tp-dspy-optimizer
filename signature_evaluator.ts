/**
 * DSPy Runtime Signature Evaluator & Telemetry Collector
 */

export interface DSPySignature {
  name: string;
  inputs: Record<string, string>;
  outputs: Record<string, string>;
}

export class SignatureEvaluator {
  public static evaluate(sig: DSPySignature, response: Record<string, any>): boolean {
    for (const key of Object.keys(sig.outputs)) {
      if (!(key in response) || response[key] === null || response[key] === '') {
        return false;
      }
    }
    return true;
  }
}
