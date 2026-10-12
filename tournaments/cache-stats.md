# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0035-20261012-085617)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 146 | 2237297 | 2059392 | 92.0% | 93.3% |
| GLM 5.3 Flash | 154 | 2133853 | 1839808 | 86.2% | 86.9% |
| GPT-6.1 Sol | 227 | 6567982 | 6031744 | 91.8% | 92.7% |
| Sonnet 5.5 | 242 | 6314386 | 6045528 | 95.7% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8877 | 101185319 | 54144000 | 53.5% | 53.5% |
| GLM 5.3 Flash | 288 | 3784493 | 3238848 | 85.6% | 86.3% |
| GPT-6.1 Sol | 7424 | 217510756 | 202383104 | 93.0% | 93.5% |
| Sonnet 5.5 | 7581 | 170536471 | 162856962 | 95.5% | 96.2% |
