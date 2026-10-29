# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0074-20261028-202920)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 169 | 9022791 | 8250880 | 91.4% | 91.7% |
| GLM 5.3 Flash | 125 | 6206107 | 5423680 | 87.4% | 87.7% |
| Muse Spark 1.3 | 153 | 5690089 | 5291137 | 93.0% | 93.4% |
| Sonnet 5.5 | 184 | 10031272 | 9366067 | 93.4% | 93.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 14951 | 366501921 | 289489538 | 79.0% | 79.3% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5560 | 181807009 | 146591556 | 80.6% | 81.2% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1240 | 27856414 | 25977504 | 93.3% | 93.8% |
| Sonnet 5.5 | 11213 | 311483382 | 296419432 | 95.2% | 95.8% |
