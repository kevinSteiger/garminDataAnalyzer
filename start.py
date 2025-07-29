from garmin_fit_sdk import Decoder, Stream


from garmin_fit_sdk import Decoder, Stream

stream = Stream.from_file("fitFiles/M7KJ5913.FIT")
decoder = Decoder(stream)
messages, errors = decoder.read()

print(errors)
print(messages)

