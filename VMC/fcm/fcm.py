import asyncio

from fcc_library import FlightControlComputer, PyMAVLinkAgent


class FlightControlModule:
    def __init__(self) -> None:
        super().__init__()

        # create the FCC objects
        self.fcc = FlightControlComputer()
        self.gps_fcc = PyMAVLinkAgent()

    async def run(self) -> None:
        asyncio.gather(
            self.fcc.run(),
            self.gps_fcc.run(),
        )

        while True:
            await asyncio.sleep(1)


if __name__ == "__main__":
    fcc = FlightControlModule()
    asyncio.run(fcc.run())
