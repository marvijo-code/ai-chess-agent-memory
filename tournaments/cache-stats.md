# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0085-20261108-115918)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 181 | 10711440 | 10020864 | 93.6% | 93.8% |
| GLM 5.3 Flash | 102 | 3969515 | 3530560 | 88.9% | 89.5% |
| Muse Spark 1.3 | 132 | 4031471 | 3740830 | 92.8% | 93.3% |
| Sonnet 5.5 | 155 | 9146740 | 8556675 | 93.5% | 94.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 17839 | 519874218 | 428353922 | 82.4% | 82.7% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 7536 | 273445201 | 228742224 | 83.7% | 84.2% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 3550 | 109973526 | 101841493 | 92.6% | 93.2% |
| Sonnet 5.5 | 14516 | 498141566 | 468569996 | 94.1% | 94.7% |
