# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0006-20261009-001831)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 98 | 1150760 | 506880 | 44.0% | 43.8% |
| GPT-6.1 Sol | 73 | 1737624 | 1545472 | 88.9% | 89.8% |
| Sonnet 5.5 | 63 | 1196428 | 1130235 | 94.5% | 95.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1492 | 16520351 | 7567616 | 45.8% | 45.7% |
| GPT-6.1 Sol | 1243 | 36576278 | 34141184 | 93.3% | 93.8% |
| Sonnet 5.5 | 1289 | 29185668 | 27925333 | 95.7% | 96.2% |
