# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0028-20261011-102906)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 204 | 2648475 | 1726976 | 65.2% | 65.3% |
| GPT-6.1 Sol | 168 | 6305300 | 6018944 | 95.5% | 95.7% |
| Sonnet 5.5 | 108 | 2160856 | 2049664 | 94.9% | 95.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7466 | 83694935 | 42772480 | 51.1% | 51.1% |
| GPT-6.1 Sol | 5999 | 175532026 | 163633152 | 93.2% | 93.7% |
| Sonnet 5.5 | 6142 | 135177604 | 129054384 | 95.5% | 96.1% |
