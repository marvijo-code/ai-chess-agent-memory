# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0036-20261012-121058)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 219 | 3798748 | 3506816 | 92.3% | 93.3% |
| GLM 5.3 Flash | 165 | 2721186 | 2480896 | 91.2% | 91.8% |
| GPT-6.1 Sol | 412 | 16542870 | 15663488 | 94.7% | 95.1% |
| Sonnet 5.5 | 256 | 6897369 | 6621098 | 96.0% | 97.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9096 | 104984067 | 57650816 | 54.9% | 54.9% |
| GLM 5.3 Flash | 453 | 6505679 | 5719744 | 87.9% | 88.6% |
| GPT-6.1 Sol | 7836 | 234053626 | 218046592 | 93.2% | 93.7% |
| Sonnet 5.5 | 7837 | 177433840 | 169478060 | 95.5% | 96.2% |
