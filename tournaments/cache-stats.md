# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0019-20261010-104326)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 279 | 2789720 | 1183872 | 42.4% | 42.2% |
| GPT-6.1 Sol | 229 | 7249021 | 6775040 | 93.5% | 93.8% |
| Sonnet 5.5 | 215 | 4879026 | 4664982 | 95.6% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5079 | 55686986 | 26477952 | 47.5% | 47.5% |
| GPT-6.1 Sol | 4122 | 119429329 | 110935168 | 92.9% | 93.4% |
| Sonnet 5.5 | 4349 | 95947115 | 91636303 | 95.5% | 96.1% |
