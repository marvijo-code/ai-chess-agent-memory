# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0051-20261019-181133)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 31 | 1559383 | 1409408 | 90.4% | 90.7% |
| DeepSeek V4.1 Flash 1017 | 25 | 759860 | 673408 | 88.6% | 89.1% |
| GLM 5.3 Flash | 25 | 1057988 | 709212 | 67.0% | 67.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 11161 | 165546596 | 110456192 | 66.7% | 66.9% |
| DeepSeek V4.1 Flash 1017 | 471 | 21175516 | 19102720 | 90.2% | 90.4% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 2224 | 61402650 | 50799440 | 82.7% | 83.2% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 603 | 31298164 | 29862221 | 95.4% | 95.8% |
| Sonnet 5.5 | 10538 | 274527705 | 261922704 | 95.4% | 96.1% |
