# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0011-20261009-135256)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 134 | 1241293 | 625408 | 50.4% | 50.3% |
| GPT-6.1 Sol | 176 | 5188118 | 4759552 | 91.7% | 92.3% |
| Sonnet 5.5 | 156 | 3365316 | 3209712 | 95.4% | 96.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2800 | 30259937 | 13630976 | 45.0% | 44.9% |
| GPT-6.1 Sol | 2513 | 74959023 | 69727744 | 93.0% | 93.5% |
| Sonnet 5.5 | 2560 | 56896470 | 54367569 | 95.6% | 96.1% |
