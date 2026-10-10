# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0015-20261010-001334)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 307 | 3492936 | 1695488 | 48.5% | 48.5% |
| GPT-6.1 Sol | 226 | 6688270 | 6299776 | 94.2% | 94.5% |
| Sonnet 5.5 | 227 | 4875300 | 4653565 | 95.5% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3914 | 42628775 | 19814912 | 46.5% | 46.4% |
| GPT-6.1 Sol | 3356 | 98306061 | 91426944 | 93.0% | 93.5% |
| Sonnet 5.5 | 3521 | 78498258 | 75007347 | 95.6% | 96.1% |
