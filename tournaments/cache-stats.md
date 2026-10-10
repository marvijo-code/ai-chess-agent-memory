# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0021-20261010-172846)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 73 | 914368 | 532992 | 58.3% | 58.3% |
| GPT-6.1 Sol | 27 | 497910 | 471552 | 94.7% | 95.5% |
| Sonnet 5.5 | 26 | 377745 | 347953 | 92.1% | 93.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5447 | 60571680 | 29320704 | 48.4% | 48.3% |
| GPT-6.1 Sol | 4458 | 129916504 | 120801024 | 93.0% | 93.4% |
| Sonnet 5.5 | 4707 | 104917991 | 100271466 | 95.6% | 96.2% |
