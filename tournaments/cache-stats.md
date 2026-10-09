# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0012-20261009-164703)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 181 | 1665753 | 884992 | 53.1% | 53.3% |
| GPT-6.1 Sol | 188 | 4910072 | 4502784 | 91.7% | 92.5% |
| Sonnet 5.5 | 233 | 5389053 | 5155190 | 95.7% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3025 | 32350746 | 14721152 | 45.5% | 45.4% |
| GPT-6.1 Sol | 2750 | 81281397 | 75549056 | 92.9% | 93.4% |
| Sonnet 5.5 | 2826 | 63181268 | 60383927 | 95.6% | 96.2% |
