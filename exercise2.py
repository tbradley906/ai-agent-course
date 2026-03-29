import anthropic

client = anthropic.Anthropic()

prompts = [
    "Hello",
    "The quick brown fox jumps over the lazy dog.",
    "Unbelievable antidisestablishmentarianism supercalifragilistic",
    "def fibonacci(n): return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)",
]

for prompt in prompts:
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=10,
        messages=[{"role": "user", "content": prompt}]
    )
    word_count = len(prompt.split())
    token_count = response.usage.input_tokens
    ratio = token_count / word_count
    print(f"Words: {word_count:3d} | Tokens: {token_count:3d} | Ratio: {ratio:.2f}x | '{prompt[:45]}'")
    