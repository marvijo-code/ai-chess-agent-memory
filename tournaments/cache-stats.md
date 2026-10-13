# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0041-20261013-124210)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 77 | 1256775 | 1190272 | 94.7% | 95.7% |
| GLM 5.3 Flash | 58 | 1224249 | 1127680 | 92.1% | 92.6% |
| GPT-6.1 Sol | 45 | 1409582 | 1244672 | 88.3% | 88.6% |
| Sonnet 5.5 | 75 | 1969528 | 1834909 | 93.2% | 94.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10061 | 122363610 | 73663232 | 60.2% | 60.3% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1176 | 19385438 | 17029056 | 87.8% | 88.6% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8978 | 271632193 | 252891520 | 93.1% | 93.6% |
| Sonnet 5.5 | 9342 | 223813384 | 214215967 | 95.7% | 96.4% |
