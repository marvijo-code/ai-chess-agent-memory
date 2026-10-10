# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0016-20261010-025717)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 180 | 1939512 | 1071360 | 55.2% | 55.3% |
| GPT-6.1 Sol | 108 | 2280834 | 2035072 | 89.2% | 90.3% |
| Sonnet 5.5 | 123 | 2071245 | 1944478 | 93.9% | 95.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4094 | 44568287 | 20886272 | 46.9% | 46.8% |
| GPT-6.1 Sol | 3464 | 100586895 | 93462016 | 92.9% | 93.4% |
| Sonnet 5.5 | 3644 | 80569503 | 76951825 | 95.5% | 96.1% |
