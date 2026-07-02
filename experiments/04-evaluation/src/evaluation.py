"""
uv run src/evaluation.py
"""
from datasets.aws_services import documents

print(f"Documents: {len(documents)}")
