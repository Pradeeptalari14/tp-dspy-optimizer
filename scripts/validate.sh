#!/usr/bin/env bash
set -eo pipefail

echo "=========================================================="
echo "⚡ Validating Stanford DSPy MIPROv2 Prompt Optimizer"
echo "=========================================================="

python3 -m py_compile dspy_compiler.py
echo "✓ dspy_compiler.py syntax validated."

python3 -m py_compile manim_flow.py
echo "✓ manim_flow.py syntax validated."

python3 -c "
from dspy_compiler import DeclarativeSignature, MIPROv2Optimizer
sig = DeclarativeSignature('TestSig', ['in1'], ['out1'])
opt = MIPROv2Optimizer(sig)
res = opt.compile([{'in1': 'val'}])
assert 'compiled_instructions' in res, 'Compilation failed'
print('✓ Unit verification passed: DSPy MIPROv2 compilation clean.')
"

echo "=========================================================="
echo "✅ All SRE validation checks passed successfully!"
echo "=========================================================="
