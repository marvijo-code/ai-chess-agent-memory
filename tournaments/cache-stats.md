# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0024-20261011-001419)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 244 | 2551467 | 1423872 | 55.8% | 55.8% |
| GPT-6.1 Sol | 214 | 6757602 | 6345344 | 93.9% | 94.2% |
| Sonnet 5.5 | 177 | 3646329 | 3460515 | 94.9% | 95.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6432 | 71387598 | 35698176 | 50.0% | 50.0% |
| GPT-6.1 Sol | 5196 | 150273424 | 139842688 | 93.1% | 93.5% |
| Sonnet 5.5 | 5421 | 119699542 | 114301423 | 95.5% | 96.1% |
