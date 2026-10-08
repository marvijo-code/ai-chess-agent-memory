# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0004-20261008-185340)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 99 | 1075432 | 588160 | 54.7% | 54.8% |
| GPT-6.1 Sol | 71 | 1704718 | 1537280 | 90.2% | 90.9% |
| Sonnet 5.5 | 72 | 1306460 | 1233350 | 94.4% | 95.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 990 | 10970109 | 5133056 | 46.8% | 46.7% |
| GPT-6.1 Sol | 779 | 22121529 | 20676224 | 93.5% | 93.8% |
| Sonnet 5.5 | 863 | 19404807 | 18578844 | 95.7% | 96.2% |
