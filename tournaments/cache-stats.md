# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0085-20261108-115918)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 159 | 9928514 | 9384576 | 94.5% | 94.7% |
| GLM 5.3 Flash | 79 | 3344281 | 2968064 | 88.8% | 89.2% |
| Muse Spark 1.3 | 89 | 2575798 | 2354964 | 91.4% | 92.0% |
| Sonnet 5.5 | 113 | 7000201 | 6575385 | 93.9% | 94.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 17817 | 519091292 | 427717634 | 82.4% | 82.7% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 7513 | 272819967 | 228179728 | 83.6% | 84.1% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 3507 | 108517853 | 100455627 | 92.6% | 93.2% |
| Sonnet 5.5 | 14474 | 495995027 | 466588706 | 94.1% | 94.7% |
