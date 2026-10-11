# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0024-20261011-001419)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 173 | 1888844 | 1047040 | 55.4% | 55.5% |
| GPT-6.1 Sol | 119 | 3419840 | 3210496 | 93.9% | 94.2% |
| Sonnet 5.5 | 92 | 1554292 | 1454277 | 93.6% | 94.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6361 | 70724975 | 35321344 | 49.9% | 49.9% |
| GPT-6.1 Sol | 5101 | 146935662 | 136707840 | 93.0% | 93.5% |
| Sonnet 5.5 | 5336 | 117607505 | 112295185 | 95.5% | 96.1% |
