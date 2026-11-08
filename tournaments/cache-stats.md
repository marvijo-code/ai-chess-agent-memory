# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0084-20261108-035328)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 129 | 5980815 | 5326080 | 89.1% | 90.4% |
| GLM 5.3 Flash | 146 | 6337898 | 5660864 | 89.3% | 89.8% |
| Muse Spark 1.3 | 122 | 3455751 | 3207461 | 92.8% | 93.7% |
| Sonnet 5.5 | 165 | 8823323 | 8188556 | 92.8% | 93.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 17603 | 506243109 | 415689090 | 82.1% | 82.4% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 7434 | 269475686 | 225211664 | 83.6% | 84.1% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 3302 | 101417064 | 93879465 | 92.6% | 93.2% |
| Sonnet 5.5 | 14256 | 483222113 | 454540932 | 94.1% | 94.7% |
