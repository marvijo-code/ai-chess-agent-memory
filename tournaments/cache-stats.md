# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0021-20261010-172846)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 110 | 1174152 | 664064 | 56.6% | 56.5% |
| GPT-6.1 Sol | 71 | 1694311 | 1585792 | 93.6% | 94.0% |
| Sonnet 5.5 | 50 | 733657 | 675450 | 92.1% | 93.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5484 | 60831464 | 29451776 | 48.4% | 48.4% |
| GPT-6.1 Sol | 4502 | 131112905 | 121915264 | 93.0% | 93.4% |
| Sonnet 5.5 | 4731 | 105273903 | 100598963 | 95.6% | 96.2% |
