# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0059-20261022-152358)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 103 | 5000734 | 4091392 | 81.8% | 82.2% |
| DeepSeek V4.1 Flash 1017 | 85 | 3498889 | 3095552 | 88.5% | 88.9% |
| GLM 5.3 Flash | 113 | 4552254 | 3591732 | 78.9% | 79.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 12813 | 251545515 | 186240768 | 74.0% | 74.3% |
| DeepSeek V4.1 Flash 1017 | 2105 | 99094038 | 87964280 | 88.8% | 89.0% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 3604 | 102549351 | 81696944 | 79.7% | 80.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 603 | 31298164 | 29862221 | 95.4% | 95.8% |
| Sonnet 5.5 | 10538 | 274527705 | 261922704 | 95.4% | 96.1% |
