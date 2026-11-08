# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0085-20261108-115918)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 221 | 12659156 | 11816192 | 93.3% | 93.6% |
| GLM 5.3 Flash | 173 | 7313837 | 6653120 | 91.0% | 91.5% |
| Muse Spark 1.3 | 138 | 4076392 | 3769058 | 92.5% | 93.2% |
| Sonnet 5.5 | 199 | 11031052 | 10242173 | 92.8% | 93.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 17879 | 521821934 | 430149250 | 82.4% | 82.8% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 7607 | 276789523 | 231864784 | 83.8% | 84.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 3556 | 110018447 | 101869721 | 92.6% | 93.2% |
| Sonnet 5.5 | 14560 | 500025878 | 470255494 | 94.0% | 94.6% |
