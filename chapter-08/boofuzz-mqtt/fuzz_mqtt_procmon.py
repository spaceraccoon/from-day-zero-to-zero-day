from boofuzz import *

procmon = ProcessMonitor('localhost', 26002)
procmon.set_options(start_commands=['/home/kali/Downloads/nanomq-0.17.5/build/nanomq/nanomq start'])

session = Session(
    target=Target(
        connection=TCPSocketConnection(
            host="localhost",
            port=1883
        ),
       monitors=[procmon]
    )
)

s_initialize("Connect")
with s_block("FixedHeader"):
    s_bit_field(
        value=0b00010000,
        width=8,
        fuzzable=False,
        name="ControlPacketTypeAndFlags"
    )
    s_size(
        block_name="Remaining",
        fuzzable=False,
        length=1,
        endian=BIG_ENDIAN,
        name="RemainingLength",
    )
    with s_block("Remaining"):
        with s_block("VariableHeader"):
            s_size(
                block_name="ProtocolName",
                fuzzable=False,
                length=2,
                endian=BIG_ENDIAN,
                name="ProtocolNameLength",
            )
            with s_block("ProtocolName"):
                s_string(value="MQTT", fuzzable=False)
            s_byte(value=5, fuzzable=False, name="ProtocolVersion")
            s_byte(value=2, fuzzable=False, name="ConnectFlags")
            s_word(
                value=60,
                fuzzable=False,
                name="KeepAlive",
                endian=BIG_ENDIAN
            )
            with s_block("Properties"):
                s_byte(value=0, fuzzable=False, name="PropertiesLength")
        with s_block("Payload"):
            s_size(
                block_name="ClientID",
                fuzzable=False,
                length=2,
                endian=BIG_ENDIAN,
                name="ClientIDLength",
            )
            with s_block("ClientID"):
                s_string(fuzzable=False, value="Client1")

s_initialize("Publish")
with s_block("FixedHeader"):
    s_bit_field(
        value=0b00110000,
        width=8,
        fuzzable=False,
        name="ControlPacketTypeAndFlags"
    )
    s_size(
        block_name="Remaining",
        fuzzable=True,
        length=1,
        endian=BIG_ENDIAN,
        name="RemainingLength",
    )
    with s_block("Remaining"):
        with s_block("VariableHeader"):
            s_size(
                block_name="TopicName",
                fuzzable=True,
                length=2,
                endian=BIG_ENDIAN,
                name="TopicNameLength",
            )
            with s_block("TopicName"):
                s_string(value="test/fuzzme", fuzzable=True)
            with s_block("Properties"):
                s_byte(value=0, fuzzable=True, name="PropertiesLength")
        with s_block("Payload"):
            s_bytes(
                fuzzable=False,
                value=b"testfuzz",
                name="ApplicationMessage"
            )

session.connect(s_get("Connect"))
session.connect(s_get("Connect"), s_get("Publish"))

session.fuzz()