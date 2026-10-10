# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0022-20261010-192853)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 211 | 2046634 | 1103872 | 53.9% | 53.7% |
| GPT-6.1 Sol | 148 | 3172086 | 2928896 | 92.3% | 92.8% |
| Sonnet 5.5 | 169 | 3375954 | 3196547 | 94.7% | 95.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5870 | 65110725 | 32014848 | 49.2% | 49.1% |
| GPT-6.1 Sol | 4774 | 137666471 | 128062208 | 93.0% | 93.5% |
| Sonnet 5.5 | 5019 | 111095779 | 106115824 | 95.5% | 96.1% |
