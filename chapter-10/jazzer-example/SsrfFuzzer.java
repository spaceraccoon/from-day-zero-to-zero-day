import com.code_intelligence.jazzer.api.FuzzedDataProvider;

public class SsrfFuzzer {
    public static void fuzzerTestOneInput(FuzzedDataProvider data) {
        SsrfExample ssrfExample = new SsrfExample();
        com.code_intelligence.jazzer.api.BugDetectors
            .allowNetworkConnections(
                (String h, Integer p) -> h.equals("example.com")
            );
        ssrfExample.getRequest(data.consumeRemainingAsAsciiString());
    }
}