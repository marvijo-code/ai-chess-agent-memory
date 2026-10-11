# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0024-20261011-001419)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 275 | 3060468 | 1806848 | 59.0% | 59.1% |
| GPT-6.1 Sol | 214 | 6757602 | 6345344 | 93.9% | 94.2% |
| Sonnet 5.5 | 200 | 4220216 | 4015121 | 95.1% | 95.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6463 | 71896599 | 36081152 | 50.2% | 50.1% |
| GPT-6.1 Sol | 5196 | 150273424 | 139842688 | 93.1% | 93.5% |
| Sonnet 5.5 | 5444 | 120273429 | 114856029 | 95.5% | 96.1% |
