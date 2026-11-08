# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0085-20261108-115918)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 159 | 9928514 | 9384576 | 94.5% | 94.7% |
| GLM 5.3 Flash | 32 | 1234221 | 1141312 | 92.5% | 93.1% |
| Muse Spark 1.3 | 74 | 2395960 | 2195302 | 91.6% | 92.0% |
| Sonnet 5.5 | 68 | 4508495 | 4238652 | 94.0% | 94.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 17817 | 519091292 | 427717634 | 82.4% | 82.7% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 7466 | 270709907 | 226352976 | 83.6% | 84.1% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 3492 | 108338015 | 100295965 | 92.6% | 93.2% |
| Sonnet 5.5 | 14429 | 493503321 | 464251973 | 94.1% | 94.7% |
