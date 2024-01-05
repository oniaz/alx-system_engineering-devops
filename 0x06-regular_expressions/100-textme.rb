#!/usr/bin/env ruby
# Extracting the sender, the reciever and the flags from given text mesages log entry and printing them to the standard output in the form:[SENDER],[RECEIVER],[FLAGS]
#   [SENDER]: The sender phone number or name (including country code if present)
#   [RECEIVER]: The receiver phone number or name (including country code if present)
#   [FLAGS]]: The flags that were used
# log_entry example = "Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:] Google,+16474951758,-1:0:-1:0:-1"

log_entry = ARGV[0]

sender_regex = /\[from:(.*?)\]/
reciever_regex = /\[to:(.*?)\]/
flags_regex = /\[flags:(.*?)\]/

sender = log_entry.scan(sender_regex).join
reciever = log_entry.scan(reciever_regex).join
flags = log_entry.scan(flags_regex).join

puts "#{sender},#{reciever},#{flags}"