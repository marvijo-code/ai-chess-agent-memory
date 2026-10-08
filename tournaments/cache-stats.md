# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0004-20261008-185340)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 244 | 2717286 | 1348992 | 49.6% | 49.6% |
| GPT-6.1 Sol | 198 | 6109786 | 5630336 | 92.2% | 92.6% |
| Sonnet 5.5 | 212 | 4534199 | 4317530 | 95.2% | 95.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1135 | 12611963 | 5893888 | 46.7% | 46.7% |
| GPT-6.1 Sol | 906 | 26526597 | 24769280 | 93.4% | 93.7% |
| Sonnet 5.5 | 1003 | 22632546 | 21663024 | 95.7% | 96.2% |
