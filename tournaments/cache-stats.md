# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0023-20261010-213538)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 55 | 528733 | 330240 | 62.5% | 63.2% |
| GPT-6.1 Sol | 33 | 741669 | 688000 | 92.8% | 93.7% |
| Sonnet 5.5 | 35 | 631201 | 595533 | 94.3% | 95.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5950 | 66032204 | 32580608 | 49.3% | 49.3% |
| GPT-6.1 Sol | 4807 | 138408140 | 128750208 | 93.0% | 93.5% |
| Sonnet 5.5 | 5067 | 112060504 | 107031236 | 95.5% | 96.1% |
