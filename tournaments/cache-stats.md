# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0020-20261010-134348)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 295 | 3970326 | 2309760 | 58.2% | 58.1% |
| GPT-6.1 Sol | 309 | 9989265 | 9394304 | 94.0% | 94.5% |
| Sonnet 5.5 | 332 | 8593131 | 8287210 | 96.4% | 96.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5374 | 59657312 | 28787712 | 48.3% | 48.2% |
| GPT-6.1 Sol | 4431 | 129418594 | 120329472 | 93.0% | 93.4% |
| Sonnet 5.5 | 4681 | 104540246 | 99923513 | 95.6% | 96.2% |
