# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0008-20261009-055507)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 152 | 1381784 | 556416 | 40.3% | 39.9% |
| GPT-6.1 Sol | 127 | 3382877 | 3112192 | 92.0% | 92.4% |
| Sonnet 5.5 | 135 | 3060056 | 2929077 | 95.7% | 96.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2149 | 23874077 | 10857344 | 45.5% | 45.4% |
| GPT-6.1 Sol | 1747 | 51402256 | 47951744 | 93.3% | 93.7% |
| Sonnet 5.5 | 1880 | 42868470 | 41022566 | 95.7% | 96.2% |
