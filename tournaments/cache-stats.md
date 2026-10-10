# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0016-20261010-025717)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 230 | 2472981 | 1309184 | 52.9% | 52.9% |
| GPT-6.1 Sol | 153 | 3230707 | 2884096 | 89.3% | 90.2% |
| Sonnet 5.5 | 151 | 2487514 | 2329859 | 93.7% | 94.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4144 | 45101756 | 21124096 | 46.8% | 46.8% |
| GPT-6.1 Sol | 3509 | 101536768 | 94311040 | 92.9% | 93.4% |
| Sonnet 5.5 | 3672 | 80985772 | 77337206 | 95.5% | 96.1% |
