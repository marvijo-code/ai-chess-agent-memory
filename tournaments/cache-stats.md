# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0040-20261013-090848)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 158 | 2625704 | 2293888 | 87.4% | 88.7% |
| GLM 5.3 Flash | 142 | 2118658 | 1666560 | 78.7% | 79.5% |
| GPT-6.1 Sol | 175 | 4951068 | 4536576 | 91.6% | 92.8% |
| Sonnet 5.5 | 207 | 5819455 | 5574265 | 95.8% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9961 | 120814263 | 72228864 | 59.8% | 59.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1118 | 18161189 | 15901376 | 87.6% | 88.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8900 | 269370670 | 250900608 | 93.1% | 93.7% |
| Sonnet 5.5 | 9131 | 217154940 | 207825633 | 95.7% | 96.4% |
