# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0004-20261008-185340)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 228 | 2607851 | 1273856 | 48.8% | 48.8% |
| GPT-6.1 Sol | 183 | 5891495 | 5445760 | 92.4% | 92.8% |
| Sonnet 5.5 | 186 | 4157271 | 3969398 | 95.5% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1119 | 12502528 | 5818752 | 46.5% | 46.5% |
| GPT-6.1 Sol | 891 | 26308306 | 24584704 | 93.4% | 93.8% |
| Sonnet 5.5 | 977 | 22255618 | 21314892 | 95.8% | 96.3% |
