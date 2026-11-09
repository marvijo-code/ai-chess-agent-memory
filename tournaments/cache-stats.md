# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0088-20261109-135130)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 155 | 8131798 | 7348608 | 90.4% | 90.7% |
| GLM 5.3 Flash | 82 | 3493765 | 3082304 | 88.2% | 88.8% |
| Muse Spark 1.3 | 150 | 6940567 | 6522670 | 94.0% | 94.3% |
| Sonnet 5.5 | 118 | 6435404 | 6001528 | 93.3% | 93.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 18600 | 563291988 | 468409858 | 83.2% | 83.5% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 8156 | 301602710 | 254472336 | 84.4% | 84.9% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 4130 | 135168496 | 125412522 | 92.8% | 93.3% |
| Sonnet 5.5 | 15168 | 534511364 | 502630564 | 94.0% | 94.6% |
