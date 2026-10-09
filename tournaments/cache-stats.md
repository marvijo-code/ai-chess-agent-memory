# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0012-20261009-164703)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 149 | 1218015 | 672384 | 55.2% | 55.5% |
| GPT-6.1 Sol | 188 | 4910072 | 4502784 | 91.7% | 92.5% |
| Sonnet 5.5 | 217 | 4986539 | 4769872 | 95.7% | 96.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2993 | 31903008 | 14508544 | 45.5% | 45.4% |
| GPT-6.1 Sol | 2750 | 81281397 | 75549056 | 92.9% | 93.4% |
| Sonnet 5.5 | 2810 | 62778754 | 59998609 | 95.6% | 96.2% |
