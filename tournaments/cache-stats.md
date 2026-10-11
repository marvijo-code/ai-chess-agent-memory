# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0025-20261011-030533)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 215 | 3020012 | 1615360 | 53.5% | 53.4% |
| GPT-6.1 Sol | 87 | 1971202 | 1812480 | 91.9% | 92.7% |
| Sonnet 5.5 | 145 | 3280958 | 3141658 | 95.8% | 96.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6678 | 74916611 | 37696512 | 50.3% | 50.3% |
| GPT-6.1 Sol | 5283 | 152244626 | 141655168 | 93.0% | 93.5% |
| Sonnet 5.5 | 5589 | 123554387 | 117997687 | 95.5% | 96.1% |
