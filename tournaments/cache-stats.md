# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0071-20261027-002235)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 133 | 6232362 | 5456384 | 87.5% | 87.9% |
| GLM 5.3 Flash | 122 | 5988717 | 5449792 | 91.0% | 91.3% |
| Haiku 5.5 | 138 | 7949342 | 7474480 | 94.0% | 94.5% |
| Muse Spark 1.3 | 112 | 2433240 | 2261691 | 92.9% | 93.5% |
| Sonnet 5.5 | 203 | 11240523 | 10572206 | 94.1% | 94.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 14317 | 332807600 | 259261442 | 77.9% | 78.2% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5038 | 155769028 | 124378492 | 79.8% | 80.4% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 741 | 39247506 | 37336701 | 95.1% | 95.5% |
| Muse Spark 1.3 | 667 | 12075493 | 11355249 | 94.0% | 94.6% |
| Sonnet 5.5 | 10741 | 285768228 | 272494910 | 95.4% | 96.0% |
