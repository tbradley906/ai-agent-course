import anthropic

client = anthropic.Anthropic()

# Prices per million tokens (from anthropic.com/pricing)
MODELS = {
    "claude-haiku-4-5":  {"input": 0.80,  "output": 4.00},
    "claude-sonnet-4-5": {"input": 3.00,  "output": 15.00},
    "claude-opus-4-5":   {"input": 15.00, "output": 75.00},
}

def estimate_cost(text: str) -> None:
    word_count = len(text.split())
    estimated_tokens = int(word_count * 1.35)

    print(f"\n{'='*55}")
    print(f"  Text length:       {len(text)} characters")
    print(f"  Word count:        {word_count} words")
    print(f"  Estimated tokens:  ~{estimated_tokens} tokens")
    print(f"{'='*55}")
    print(f"  {'Model':<22} {'Input cost':>12} {'Output cost':>12}")
    print(f"  {'-'*48}")

    for model_name, prices in MODELS.items():
        input_cost  = (estimated_tokens / 1_000_000) * prices["input"]
        output_cost = (estimated_tokens / 1_000_000) * prices["output"]
        print(f"  {model_name:<22} ${input_cost:>10.5f}  ${output_cost:>10.5f}")

    print(f"{'='*55}")
    print(f"  Note: output cost assumes same length as input\n")

if __name__ == "__main__":
    print("\nPaste your text below. Press Enter twice when done:\n")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    user_text = "\n".join(lines)
    if user_text.strip():
        estimate_cost(user_text)
    else:
        print("No text entered.")