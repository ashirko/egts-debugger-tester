import scenario

sock = scenario.start_scenario()
auth_packet = b"\x01\x00\x00\x0b\x00\x0f\x00\x01\x00\x01\x06\x08\x00\x01\x00\x38\x01\x01\x05\x05\x00\x00" \
              b"\xef\x03\x00\x00\x07\xcd"
sock.send(auth_packet)
_ = sock.recv(1024)
sock.send(auth_packet)
_ = sock.recv(1024)
sock.close()