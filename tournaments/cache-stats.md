# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0023-20261010-213538)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 237 | 2709386 | 1691136 | 62.4% | 62.6% |
| GPT-6.1 Sol | 176 | 5176331 | 4816000 | 93.0% | 93.5% |
| Sonnet 5.5 | 181 | 4108259 | 3923560 | 95.5% | 96.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6132 | 68212857 | 33941504 | 49.8% | 49.7% |
| GPT-6.1 Sol | 4950 | 142842802 | 132878208 | 93.0% | 93.5% |
| Sonnet 5.5 | 5213 | 115537562 | 110359263 | 95.5% | 96.1% |
