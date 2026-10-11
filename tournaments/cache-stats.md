# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0026-20261011-055315)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 200 | 2005614 | 1061376 | 52.9% | 52.8% |
| GPT-6.1 Sol | 106 | 2110069 | 1915904 | 90.8% | 91.5% |
| Sonnet 5.5 | 133 | 2896451 | 2756764 | 95.2% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6972 | 77839193 | 39225344 | 50.4% | 50.3% |
| GPT-6.1 Sol | 5458 | 155943182 | 145088640 | 93.0% | 93.5% |
| Sonnet 5.5 | 5784 | 127504632 | 121742573 | 95.5% | 96.1% |
