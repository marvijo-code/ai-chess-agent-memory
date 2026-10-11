# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0026-20261011-055315)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 272 | 2951883 | 1646080 | 55.8% | 55.7% |
| GPT-6.1 Sol | 192 | 6320622 | 5950464 | 94.1% | 94.6% |
| Sonnet 5.5 | 176 | 3824383 | 3639389 | 95.2% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7044 | 78785462 | 39810048 | 50.5% | 50.5% |
| GPT-6.1 Sol | 5544 | 160153735 | 149123200 | 93.1% | 93.6% |
| Sonnet 5.5 | 5827 | 128432564 | 122625198 | 95.5% | 96.1% |
