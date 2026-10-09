# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0007-20261009-031124)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 231 | 2709749 | 1222528 | 45.1% | 45.1% |
| GPT-6.1 Sol | 162 | 4286763 | 3922304 | 91.5% | 92.1% |
| Sonnet 5.5 | 156 | 2981271 | 2819094 | 94.6% | 95.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1935 | 21789283 | 10056704 | 46.2% | 46.1% |
| GPT-6.1 Sol | 1536 | 44553462 | 41521664 | 93.2% | 93.6% |
| Sonnet 5.5 | 1698 | 38781473 | 37112705 | 95.7% | 96.2% |
